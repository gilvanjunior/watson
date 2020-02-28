/**
  *
  * main() será executado ao clicar em "Run This Action".
  * 
  * @author     Gilvan Junior
  * @company    Magic
  * @contact    https://www.linkedin.com/in/gilvanjunior/
  *
  */
  
const AssistantV1 = require('ibm-watson/assistant/v1');
var Cloudant = require("@cloudant/cloudant");

function main(params) {
    
    const assistant = new AssistantV1({
      iam_apikey: params.IAM_APIKEY,
      version: params.WDC_VERSION,
      url: params.WDC_URL
    });
    
    const cloudant = Cloudant({
        account: params.CLOUDANT_ACCOUNT,
        password: params.CLOUDANT_PASSWORD
    });
    
    console.log(JSON.stringify(params))

    const versioning_db = cloudant.db.use(params.CLOUDANT_DBNAME);
    
    return new Promise(function(resolve, reject){
        var wdc_params = {
            workspace_id: params.WDC_WORKSPACEID,
            _export: true
        };
        assistant.getWorkspace(wdc_params)
          .then(res => {
            var d = new Date();
            d.setHours(d.getHours() - 3);
            var horario = d.toISOString();
          
            res._id = params.WDC_PREFIX + horario;
              
            versioning_db.insert(res, function (err, body, header) {
                if (err) return reject(err);
                return resolve({ "message": "Backup realizado com sucesso!" });
             });
          })
          .catch(err => {
            console.log(err)
          });
    });
    
}