package com.web.demo1.service;


import com.web.demo1.bean.city.*;
import com.web.demo1.bean.district.*;
import java.util.List;

public interface BigdataService {
    public List<City> queryCity();
    public List<Area> queryArea();
    public  List<Area> queryAreaSold();
    public  List<District> queryDsold();
    public  List<District> queryDrent();
    public  List<Trend> queryTrend();
}
