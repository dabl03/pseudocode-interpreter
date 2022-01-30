Resuelto:{
Ingresa:
si 1==1://Lo que trato de hacer es anidar los if.
START;
 imprimir("inicio");
 si 2==1:
 START;
  imprimir("ERROR;");
 END;
 si 1==1:
 START;
  imprimir("2 nivel");
  si 1==1:
  START;
   imprimir("3 nivel");
   si 2==3:
   START;
    imprimir("3 ERROR");
   END;
  END;
 END;
END;

Y te dara este error:
>>> si 1==1:
... START;
 ... imprimir("inicio");
 ... si 1==2://Si no pusieramos esto a dentro de un if entonces no daria error.
 ... START;
  ... imprimir("ERROR");
  ... END;
 ... END;
inicio
Traceback (most recent call last):
  File "C:\Users\RUBI LONDOÑO\Documents\pseudocode-interpreter\lexer.py", line 621, in <module>
    variables = run(runner)
  File "C:\Users\RUBI LONDOÑO\Documents\pseudocode-interpreter\lexer.py", line 546, in run
    result_cond = proc_cond(pgman, tkn, scope_vars, Func=Func)
  File "C:\Users\RUBI LONDOÑO\Documents\pseudocode-interpreter\lexer.py", line 471, in proc_cond
    if expr: expr=run(pgma, Func=Func)
  File "C:\Users\RUBI LONDOÑO\Documents\pseudocode-interpreter\lexer.py", line 546, in run
    result_cond = proc_cond(pgman, tkn, scope_vars, Func=Func)
  File "C:\Users\RUBI LONDOÑO\Documents\pseudocode-interpreter\lexer.py", line 474, in proc_cond
    if next(pgma).texto != ";": exit("EOF ERROR")
  File "C:\Users\RUBI LONDOÑO\Documents\pseudocode-interpreter\lexer.py", line 172, in __next__
    return next(self.tokens)
StopIteration
}
Problema:{
>>> func hola():
... START;
 ... imprimir("hola");
 ... func o():
 ... START;
  ... imprimir("como estas");//Como nunca llamo a o() no deberia aparecer este mensaje.
  ... END;
 ... END;
>>> hola();
hola
como estas
>>>
}