import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
@app.blob_input(arg_name="inputBlob", path="wangbillsmartai/githubprojectdata/data.json", connection="JsonDataStorage")
@app.blob_output(arg_name="outputBlob", path="wangbillsmartai/githubprojectdata/data.json", connection="JsonDataStorage")
def http_trigger(req: func.HttpRequest, inputBlob: func.InputStream, outputBlob: func.Out[str]) -> func.HttpResponse:
    logging.info('Processing JSON data.')

    try:
        # Read the input JSON from the blob
        input_json = json.loads(inputBlob.read().decode('utf-8'))

        logging.info(f"Input JSON: {input_json}")

        # Format the JSON with indentation
        formatted_json = json.dumps(input_json, indent=4)

        logging.info(f"Formatted JSON: {formatted_json}")
        # Write the formatted JSON to the output blob (overwriting the same path)
        outputBlob.set(formatted_json)

        return func.HttpResponse("JSON formatted and saved successfully.", status_code=200)
    except Exception as e:
        logging.error(f"Error processing JSON data: {str(e)}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)