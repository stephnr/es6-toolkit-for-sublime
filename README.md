# ES6-Toolkit for Sublime Text
A toolkit containing various commands and snippets for using ES6 today in Sublime

## Download Details in >> [Package Control](https://packagecontrol.io/packages/ES6-Toolkit)

----------------------------------------------------------------------------------
                                  IMPORTANT
----------------------------------------------------------------------------------

In order to be able to run the ES6 Compiler, you will need to install the NPM module
`babel` globally. Please run the following command to install babel:

```bash
npm install -g babel
```

----------------------------------------------------------------------------------

## Features

The ES6-Toolkit comes pre-packages with lots of cool tools. Below is a short list
with links to more information in the Wiki Pages:

1. ES6 Completions => [Wiki Link](https://github.com/lukehoban/es6features)
2. Compile entire JS files to JS compatible code using Babel

## Coming Soon

1. ES6 Inline Compiling
2. Compile entire projects to ES5 using Babel

-----------------------------------------------------------------------------------

ES6 Completions
---

#### [Arrow] Arrow Functions

```js
var => function
```

#### [Class] Class Declaration

```js
class Classname extends AnotherClass {
  constructor(args) {
    // code
  }

  // methods
}
```

#### [generator] Generator

```js
var generator = {
  [Symbol:iterator]: function() {
	var pre = 0, cur = 1;
	for(;;) {
	  var temp = pre;
	  pre = cur;
	  cur += temp;
	  yield cur;
	}
  }
}
```

#### [let:iterator] Iterator using Let

```js
let v = {
  [Symbol.iterator]() {
    let pre = 0, cur = 1;
    return {
	  next() {
	    [pre, cur] = [cur, pre + cur];
	    return { done: false, value: cur };
	  }
	}
  }
}
```

#### [let] Let

```js
let x = 'something';
```

#### [Map] Map

```js
var map = new Map();
```

#### [WeakMap] WeakMap

```js
var map = new WeakMap();
```

#### [import] Module Import

```js
import * as mod from 'lib/package';
```

#### [System.import] Module Import via System

```js
System.import('my-module').then(function(m) {
	// code...
});
```

#### [export:variable] Module Exporting

```js
export var myvar = value;
```

#### [Loader] Module Loading using Loader

```js
var loader = new Loader({
  global: fixup(window)
});
```

#### [System.get] Module Loading using Get

```js
System.get('module');
```

#### [System.set] Module Loading using Set

```js
// WARNING: System.set is not finalized yet
System.set('jquery', Module({$: $}));
```

#### [object] Object Literal

```js
var obj = {
  __proto__: theProtoObj,
  handler,
  toString() {
    return "object";
  }
}
```

#### [Promise] Promise

```js
Promise((resolve, reject) => {
  // code...
});
```

#### [Proxy] Proxy

```js
var p = new Proxy(target, handler);
```

#### [Set] Set

```js
var set = new Set();
```

#### [WeakSet] WeakSet

```js
var set = new WeakSet();
```

#### [string] String Templates

```js
${some_var}
```

#### [ForLet] For Loop using Let

```js
for (let value of iterable) {
  // do something
}
```

...and more!!!

Support
----

To learn more about the features and settings, please visit
https://github.com/Stephn-R/ES6-Toolkit-for-Sublime

If you are having trouble, please contact me at steprodriguez10@gmail.com
