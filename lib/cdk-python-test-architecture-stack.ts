import * as cdk from "@aws-cdk/core";
import { Table, AttributeType } from "@aws-cdk/aws-dynamodb";
import { RemovalPolicy } from "@aws-cdk/core";
import { Function, Runtime, Code, LayerVersion } from "@aws-cdk/aws-lambda";
import * as path from "path";

export class CdkPythonTestArchitectureStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Lambda Layer
    const customLayer = new LayerVersion(this, "MyLayer", {
      layerVersionName: "customLayer",
      code: Code.fromAsset("layer_builder/table_model"),
      compatibleRuntimes: [Runtime.PYTHON_3_8],
      description: "Layer sample",
    });
    const customLayerResource = customLayer.node.findChild('Resource') as cdk.CfnResource;
    customLayerResource.applyRemovalPolicy(cdk.RemovalPolicy.RETAIN);

    const requestsLayer = new LayerVersion(this, "MyLayer2", {
      layerVersionName: "requestsLayer",
      code: Code.fromAsset("layer_builder/requests"),
      compatibleRuntimes: [Runtime.PYTHON_3_8],
      description: "requests layer",
    });
    const requestsLayerResource = customLayer.node.findChild('Resource') as cdk.CfnResource;
    requestsLayerResource.applyRemovalPolicy(cdk.RemovalPolicy.RETAIN);

    // The code that defines your stack goes here
    const fn = new Function(this, "MyFunction", {
      runtime: Runtime.PYTHON_3_8,
      handler: "index.handler",
      code: Code.fromAsset(path.join(__dirname, "../resources/get_data")),
      layers: [customLayer, requestsLayer],
    });
    const table1 = new Table(this, "SampleTable1", {
      tableName: "sample_table1",
      partitionKey: { name: "id", type: AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY,
    });
    const table2 = new Table(this, "SampleTable2", {
      tableName: "sample_table2",
      partitionKey: { name: "id", type: AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY,
    });
    table1.grantReadWriteData(fn);
    table2.grantReadWriteData(fn);
  }
}
