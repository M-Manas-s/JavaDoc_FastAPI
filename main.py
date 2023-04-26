import requests
import json
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import requests
from fastapi.responses import RedirectResponse
import os
from fastapi.responses import FileResponse
from fastapi.responses import PlainTextResponse

app = FastAPI()
origins = [
    "http://localhost:3001",
    "http://localhost:3000",
]

imports = {     "thread" : "java.lang.*;",
                "regex" : "java.util.regex.*;",
                "math" : "java.math.*;",
                "linkedlist" : "java.util.LinkedList;",
                "scanner" : "java.util.Scanner;",
                "array" : "java.util.Arrays;",
                "set" : "java.util.TreeSet;",
                "hashset" : "java.util.HashSet;",
                "hashmap" : "java.util.HashMap;",
                "treemap" : "java.util.TreeMap;",
                "orderedset" : "java.util.TreeSet;",
                "unorderedset" : "java.util.HashSet;",
                "arraylist" : "java.util.ArrayList;",
                "mimeencodes" : "java.util.Base64;",
                "exception" : "java.util.*;",
                "customexception" : "java.util.*;",
                "thread" : "java.util.*;",
                "stack" : "java.util.*;",
                "jdbc" : "java.sql.*;",
                 }

exception = [   "NumberFormatException", 
                "ArithmeticException", 
                "InputMismatchException", 
                "ArrayIndexOutOfBoundsException" ]

codes = {    "scanner" : "  Scanner sc = new Scanner(System.in);",
            "array" : " int arr[] = new int[5];",
            "linkedlist" : "LinkedList<String> list=new LinkedList<String>();",
            "swap" : "Collections.swap(list,1,4);",
            "sort" : "Collections.sort(list);",
            "reverse" : "Collections.reverse(list);",
            "shuffle" : "Collections.shuffle(list);",
            "binarysearch" : "Collections.binarySearch(list, \"A\");",
            "revsort" : "Collections.sort(list,Collections.reverseOrder());",
            "set" : "TreeSet<Integer> ts=new TreeSet<Integer>();",
            "hashset" : "HashSet<Integer> hs=new HashSet<Integer>();",
            "hashmap" : "HashMap<Integer,Integer> hm=new HashMap<Integer,Integer>();",
            "hashmapput" : "hm.put(1,2);",
            "hashmapinsert" : "hm.put(1,2);",
            "hashmapget" : "hm.get(1);",
            "treemap" : "TreeMap<Character,Integer> map=new TreeMap<Character,Integer>();",
            "orderedset" : "TreeSet<Integer> ts = new TreeSet<Integer>();",
            "unorderedset" : "HashSet<Integer> hs=new HashSet<Integer>();",
            "setadd" : "ts.add(1);",
            "setremove" : "ts.remove(1);",
            "setaddall" : "ts.addAll(hs);",
            "setremoveall" : "ts.removeAll(hs);",
            "setretainall" : "ts.retainAll(hs);",
            "linetochararray" : " for(char c : line.toCharArray())",
            "arraylist" : "ArrayList<Integer> list=new ArrayList<Integer>();",
            "arraylistadd" : "list.add(1);",
            "arraylistget" : "list.get(1);",
            "arraylistremove" : "list.remove(1);",
            "loopmap" : "for(Map.Entry<Character,Integer> entry : map.entrySet()) System.out.print(entry.getKey() +\":\"+entry.getValue()+" ");",
            "loopset" : "for(Integer i : ts) System.out.print(i+\" \");",
            "customexception" : """class DivisiblebyFiveException extends Exception 
                            {
                                public DivisiblebyFiveException(String message)
                                {
                                    super(message);
                                }
                            }""",
            "jdbc" : """Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/ri_db","test","test123");
            Statement st=con.createStatement();
            ResultSet rs=st.executeQuery("select name,phone from students where sid="+id);
            while(rs.next())
                System.out.println(rs.getString(1)+" "+rs.getString(2));
            st.close();
            con.close()""",
            "jdbcdrivermanager" : "Connection conn = DriverManager.getConnection(url, uname, pass);",
            "jdbcstatement" : "Statement st = conn.createStatement();",
            "jdbcresultset" : "ResultSet rs = st.executeQuery(query);",
            "jdbcwhile" : "while(rs.next())",
            "jdbcinsert" : "st.executeUpdate(\"insert into students values(1,'Rishabh','1234567890')\");",
            "jdbcupdate" : "int count = st.executeUpdate(\"update students set name='Rishabh' where sid=1\");",
            "throwexception" : "throw new Exception(\"n or p should not be negative.\");",
            "sortedlist" : "Collections.sort(list); ArrayList<Integer> list = new ArrayList<Integer>(treeSet);",
            "thread" : """ class B extends Thread
                        {
                            public void run()
                            {
                                for(int i=1;i<=10;i++)
                                {
                                    System.out.print(" "+i*5);
                                }
                            }
                        }
                        """,
            "threadstart" : "B b=new B();b.start();",
            "queue" : "Queue<Integer> queue = new LinkedList<>();",
            "queueadd" : "queue.add(1);",
            "queuefront" : "queue.remove();",
            "queuepop" : "queue.remove();",
            "stack" : "Stack<Character> stack = new Stack<>();",
            "stackpush" : "stack.push(c);",
            "stackpop" : "stack.pop();",
            "stackempty" : "stack.isEmpty();",
            "testcasesstring" : "while(scanner.hasNextLine())",
            "testcasesint" : "sc.hasNextInt()",
            "mimeencodes" : """Base64.Encoder encoder = Base64.getMimeEncoder();  
                            String message = ip.next();
                            String eStr = encoder.encodeToString(message.getBytes());""",
            "throwexception" : "throw new DivisiblebyFiveException(\"Number should not be divide by five\");"  }

inputs = {   "int" : "X = sc.nextInt();",
            "string" : "X = sc.next();",
            "line" : "String line = scanner.nextLine();",
            "char" : "char c = scanner.next().charAt(0);",
            "double" : "double X = sc.nextDouble();",
            "float" : "float X = sc.nextFloat();",
            "long" : "long X = sc.nextLong();",
            "short" : "short X = sc.nextShort();",
             }

@app.get("/")
async def redirect_to_website():
    return RedirectResponse(url="https://lms.vit.ac.in/")

@app.get("/codes/")
async def read_item(args: str = "scanner"):
    return codes[args]

@app.get("/inputs/")
async def read_item(args: str = "string"):
    return inputs[args]

@app.get("/imports/")
async def read_item(args: str = "thread"):
    return imports[args]

@app.get("/index/")
async def read_item(args: str = "default"):
    if ( args == "default" ):
        return "codes, inputs, imports => to find keys = /index/?args=codes"
    if ( args == "codes" ):
        return " ".join(codes.keys()) + "       \n USE AS => /codes/?args=<key>"
    if ( args == "inputs" ):
        return " ".join(inputs.keys()) + "       \n USE AS => /inputs/?args=<key>"
    if ( args == "imports" ):
        return " ".join(imports.keys()) + "       \n USE AS => /imports/?args=<key>"

@app.get("/exception/")
def fnc():
    return " ".join(exception)



# import uvicorn

# if __name__ == "__main__":
#   uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)
