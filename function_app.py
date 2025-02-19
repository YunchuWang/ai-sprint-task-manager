import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
@app.blob_input(name="inputBlob", path="samples-workitems/{name}", connection="AzureWebJobsStorage")
@app.blob_output(name="outputBlob", path="samples-workitems/{name}-copy", connection="AzureWebJobsStorage")
def http_trigger(req: func.HttpRequest, inputBlob: func.InputStream) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )