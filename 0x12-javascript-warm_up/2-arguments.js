#!/usr/bin/node
// This is a script that prints a message depending
// on the number of argument passed

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
