#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { CdkPythonTestArchitectureStack } from '../lib/cdk-python-test-architecture-stack';

const app = new cdk.App();
new CdkPythonTestArchitectureStack(app, 'CdkPythonTestArchitectureStack');
