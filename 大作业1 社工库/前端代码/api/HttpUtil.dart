import 'package:dio/dio.dart';

class HttpUtil {

  ///
  /// 静态[HttpUtil]对象[_instance],用于网络请求
  ///
  static final HttpUtil _instance = HttpUtil._internal();
  Dio _client;
  // ignore: non_constant_identifier_names

  factory HttpUtil() => _instance;

  HttpUtil._internal(){
    if (_client == null) {
      BaseOptions options = new BaseOptions(
        connectTimeout: 1000 * 10,
        receiveTimeout: 3000,
        responseType: ResponseType.json,
      );
      _client = new Dio(options);
    }
  }
  ///
  /// get方法，传入参数：
  /// path:在基础URL[BASE_URL]之后添加的路径
  /// params：参数键值对
  ///
  Future<Response<Map<String, dynamic>>> get(String path, [Map<String, dynamic> params]) async {
    Response<Map<String, dynamic>> response;
    if(params != null){
      response = await _client.get(path,queryParameters: params);
    }else{
      response = await _client.get(path);
    }
    return response;
  }


  ///
  /// post方法，传入参数：
  /// path:在基础URL[BASE_URL]之后添加的路径
  /// params：参数键值对
  ///
  Future<Response<Map<String, dynamic>>> post(String path, [Map<String, dynamic> params]) async {
    Response<Map<String, dynamic>> response;
    if(params != null || params.isNotEmpty){
      print('params = ' + params.toString());
      response = await _client.post(path,queryParameters: params);
    }else{
      response = await _client.post(path);
    }
    return response;
  }
}


