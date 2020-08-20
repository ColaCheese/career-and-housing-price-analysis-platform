package com.web.demo1.controller;


import com.web.demo1.bean.city.*;
import com.web.demo1.bean.district.*;
import com.web.demo1.service.BigdataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

//映射 ajax路径 接受jsp请求 controller调用model(dao service)方法 接受相应返回给jsp
@Controller
@RequestMapping("/dataController")
public class BigdataController {

    @Autowired
    private BigdataService bigdataService;

    @RequestMapping("LZHcity")
    @ResponseBody
    public Object queryCityList() {
        List<City> list = bigdataService.queryCity();
        return list;
    }
    @RequestMapping("LZHarea")
    @ResponseBody
    public Object queryAreaList() {
        List<Area> list = bigdataService.queryArea();
        return list;
    }
    @RequestMapping("areaSold")
    @ResponseBody
    public Object queryAreaSoldList() {
        List<Area> list = bigdataService.queryAreaSold();
        return list;
    }
    @RequestMapping("Dsold")
    @ResponseBody
    public Object queryDsoldList() {
        List<District> list = bigdataService.queryDsold();
        return list;
    }
    @RequestMapping("Drent")
    @ResponseBody
    public Object queryDrentList() {
        List<District> list = bigdataService.queryDrent();
        return list;
    }

    @RequestMapping("Trend")
    @ResponseBody
    public Object queryTrendList() {
        List<Trend> list = bigdataService.queryTrend();
        return list;
    }
}
