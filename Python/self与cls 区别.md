#### self表示一个具体的实例本身。如果用了staticmethod，那么就可以无视这个self，将这个方法当成一个普通的函数使用。

#### cls表示这个类本身。



@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
 @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
 如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
 而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。



其实就是 staticmethod，这个方法，不能在类内调用其他的类的方法而 classmethod 可调用其他的方法，因为有 cL 这个参数。

 Staticmethod 与 Classmethod！的方法与 seL 这个方法的区别，就是 sef 必须使用实例化对象，也就是 a=A(), a.方法（而另外两个方法只用，A 方法即可