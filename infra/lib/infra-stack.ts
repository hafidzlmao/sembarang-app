import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as api_gateway from "aws-cdk-lib/aws-apigateway";
import * as dotenv from "dotenv";
import { Lambda } from 'aws-cdk-lib/aws-ses-actions';

dotenv.config();

// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class InfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const layer = new lambda.LayerVersion(this, "BaseLayer", {
      code: lambda.Code.fromAsset("baselayer_lambda/layer.zip"),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
    });

    const LambdaAPI = new lambda.Function(this, "ApiFunction", {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset("../app/"),
      handler: "sembarang_api.handler",
      layers: [layer],
      environment: {
        OPENAI_API_KEY: process.env.OPENAI_API_KEY ?? "",
      },
    });

    const sembarangAPI = new api_gateway.RestApi(this, "RESTAPI", {
      restApiName: "Sembarang API",
    });

    sembarangAPI.root.addProxy({
      defaultIntegration: new api_gateway.LambdaIntegration(LambdaAPI),
    });
  }
}
