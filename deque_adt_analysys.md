В целом, это первое задание, где у меня архитектурно и по АТД всё совпадает с эталонным решением.

Единственное, что могу подметить в части реализации, это наличие в базовом абстрактном классе обоих методов `get_head()` и `get_tail()`, 
в то время как в эталонном решении в базовом классе реализован только метод `get_head()` (только с другим названием).

Наверное, при жёстком разграничении структур `Queue` и `Deque` имеет смысл в базовом классе определить только метод `get_head()`, 
а уже для `Deque` расширить добавлением метода `get_tail()`. 

В целом, с точки зрения функциональности двух структур, наличие возможности получить значение из голова и хвоста для `Queue` может 
сбивать с толку и быть лишним компонентом реализации.
