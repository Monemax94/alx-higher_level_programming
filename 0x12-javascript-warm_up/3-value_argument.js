#!/usr/bin/node

// This is a script that prints the first argument passed to it

if (process.argv[2] === undifined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
