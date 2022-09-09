import 'package:flutter/material.dart';
import 'package:she_gong_ku/api/Common_api.dart';
import 'package:she_gong_ku/api/HttpUtil.dart';
import 'package:dio/dio.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double width, height;
  TextEditingController keyController;
  String selectedDB = "点击选择数据库";
  String searchedDB = "";
  List dataList;
  bool isFetchingData = false;

  Widget searchBar(){
    return Container(
      width: width,
      height: 80,
      padding: EdgeInsets.all(20),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Expanded(
            flex: 3,
            child: TextButton(
              onPressed: selectDB,
              style: ButtonStyle(
                alignment: Alignment.center
              ),
              child: Text(
                  selectedDB
              ),
            ),
          ),
          Spacer(
            flex: 1,
          ),
          Expanded(
            flex: 8,
            child: TextField(
              controller: keyController,
              decoration: InputDecoration(
                fillColor: Colors.white,
                filled: true,
                border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                    borderSide: BorderSide(color: Colors.transparent)
                ),
                contentPadding: EdgeInsets.all(10),
                hintText: "输入关键字",
                hintStyle: TextStyle(
                  color: Colors.grey[300]
                )
              ),
            ),
          ),
          Spacer(
            flex: 1,
          ),
          Expanded(
            flex: 2,
            child: TextButton(
              onPressed: subbmit,
              child: Text(
                "查询"
              ),
            ),
          )
        ],
      ),
    );
  }

  Widget tableItem(double height, String DBname, {
    String ID,
    String QQNum,
    String Nick,
    String Age,
    String Gender,
    String Auth,
    String QunNum,
    String MastQQ,
    String CreateDate,
    String Title,
    String Class,
    String QunText
  }){
    if('qqq' == DBname){
      return Container(
        width: width,
        height: height,
        padding: EdgeInsets.all(20),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Expanded(
              flex: 2,
              child: Center(
                child: Text(
                    ID??"null"
                ),
              )
            ),
            Expanded(
              flex: 3,
              child: Center(
                child: Text(
                    QQNum??"null"
                ),
              )
            ),
            Expanded(
              flex: 3,
              child: Center(
                child: Text(
                    Nick??"null"
                ),
              )
            ),
            Expanded(
              flex: 2,
              child: Center(
                child: Text(
                    Age??"null"
                ),
              )
            ),
            Expanded(
              flex: 2,
              child: Center(
                child: Text(
                    Gender??"null"
                ),
              )
            ),
            Expanded(
              flex: 2,
              child: Center(
                child: Text(
                    Auth??"null"
                ),
              )
            ),
            Expanded(
              flex: 3,
              child: Center(
                child: Text(
                    QunNum??"null"
                ),
              )
            ),
          ],
        ),
      );
    }else{
      return Container(
        width: width,
        height: height,
        padding: EdgeInsets.all(20),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Expanded(
                flex: 3,
                child: Center(
                  child: Text(
                      QunNum??"null"
                  ),
                )
            ),
            Expanded(
                flex: 2,
                child: Center(
                  child: Text(
                      MastQQ??"null"
                  ),
                )
            ),
            Expanded(
                flex: 3,
                child: Center(
                  child: Text(
                      CreateDate??"null"
                  ),
                )
            ),
            Expanded(
                flex: 4,
                child: Center(
                  child: Text(
                      Title??"null"
                  ),
                )
            ),
            Expanded(
                flex: 2,
                child: Center(
                  child: Text(
                      Class??"null"
                  ),
                )
            ),
            Expanded(
                flex: 5,
                child: Center(
                  child: Text(
                      QunText??"null"
                  ),
                )
            ),
          ],
        ),
      );
    }
  }

  Widget showtable(){
    return Expanded(
      child: LayoutBuilder(
        builder: (context, constraints){
          return Container(
            width: constraints.maxWidth,
            height: constraints.maxHeight,
            child: dataList == null || isFetchingData ?
            Center(
              child: isFetchingData ?
              CircularProgressIndicator():Text("您还未进行查询")
            )
                :
            ListView.separated(
                itemBuilder: (context, index){
                  if(searchedDB == 'qqq'){
                    if(index == 0){
                      return tableItem(
                        150,
                        "qqq",
                        QunNum: "群号",
                        ID: "ID",
                        QQNum: "QQ号",
                        Nick: "昵称",
                        Age: "年龄",
                        Gender: "性别",
                        Auth: "Auth",
                      );
                    }else{
                      return tableItem(
                        80,
                        "qqq",
                        QunNum: dataList[index - 1]['QunNum'],
                        ID: dataList[index - 1]["ID"],
                        QQNum: dataList[index - 1]["QQNum"],
                        Nick: dataList[index - 1]["Nick"],
                        Age: dataList[index - 1]["Age"],
                        Gender: dataList[index - 1]["Gender"],
                        Auth: dataList[index - 1]["Auth"],
                      );
                    }
                  }else{
                    if(index == 0){
                      return tableItem(
                        150,
                        "list",
                        QunNum: "群号",
                        MastQQ: "群人数",
                        CreateDate: "创建时间",
                        Title: "群名",
                        Class: "Class",
                        QunText: "群口号"
                      );
                    }else{
                      return tableItem(
                        80,
                           "list",
                          QunNum: dataList[index - 1]['QunNum'],
                          MastQQ: dataList[index - 1]["MastQQ"],
                          CreateDate: dataList[index - 1]["CreateDate"],
                          Title: dataList[index - 1]["Title"],
                          Class: dataList[index - 1]["Class"],
                          QunText: dataList[index - 1]["QunText"]
                      );
                    }
                  }
                },
                separatorBuilder: (context, index){
                  return Container();
                },
                itemCount: dataList.length > 100 ? 100 : dataList.length
            ),
          );
        },
      ),
    );
  }

  @override
  void didChangeDependencies() {
    // TODO: implement didChangeDependencies
    super.didChangeDependencies();
    Size size = CommonApi.initParameter(context);
    width = size.width;
    height = size.height;
    keyController = TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          searchBar(),
          showtable()
        ],
      ),
    );
  }

  void selectDB(){
    showModalBottomSheet(context: context, builder: (context){
      return Container(
        width: width,
        height: 200,
        child: Column(
          children: [
            Expanded(
              flex: 1,
              child: GestureDetector(
                  behavior: HitTestBehavior.opaque,
                  onTap: (){
                    selectedDB = "list";
                    setState(() {});
                    Navigator.of(context).pop();
                  },
                  child: Center(
                    child: Text(
                        "list"
                    ),
                  ),
              ),
            ),
            Expanded(
              flex: 1,
              child: GestureDetector(
                behavior: HitTestBehavior.opaque,
                onTap: (){
                  selectedDB = "qqq";
                  setState(() {});
                  Navigator.of(context).pop();
                },
                child: Center(
                  child: Text(
                      "qqq"
                  ),
                ),
              ),
            )
          ],
        ),
      );
    });
  }

  void subbmit() async {
    if(selectedDB != "点击选择数据库"){
      isFetchingData = true;
      setState(() {
      });
      searchedDB = selectedDB;
      String key = keyController.text;
      Map<String, dynamic> param = Map<String, dynamic>();
      param['dbname'] = searchedDB;
      param['key'] = key;
      Response<Map<String, dynamic>> response = await HttpUtil().get('http://127.0.0.1:8000/showData/', param);
      dataList = response.data['data'];
      print('$dataList');
      isFetchingData = false;
      setState(() {
      });
    }
  }
}
