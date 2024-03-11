#!/usr/bin/node

switch (process.argv[2]) {
  case undefined: {
    console.log('No argument');
    break;
  }
  default: {
    console.log(process.argv[2]);
  }
}
