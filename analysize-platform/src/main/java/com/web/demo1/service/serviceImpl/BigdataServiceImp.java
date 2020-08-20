package com.web.demo1.service.serviceImpl;

import com.web.demo1.bean.city.*;
import com.web.demo1.bean.district.*;
import com.web.demo1.dao.BigdataMapper;
import com.web.demo1.service.BigdataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

//具体实现
@Service
public class BigdataServiceImp implements BigdataService {
    @Autowired
    private BigdataMapper bigdataMapper;

    //对sql数据具体操作
    public List<City> queryCity() {
        return bigdataMapper.selectCityRent();
    }
    public List<Area> queryArea() {
        return bigdataMapper.selectAreaRent();
    }
    public  List<Area> queryAreaSold(){
        return bigdataMapper.selectCitySold();
    }
    public  List<District> queryDsold(){
        return bigdataMapper.selectDsold();
    }
    public  List<District> queryDrent(){
        return bigdataMapper.selectDrent();
    }
    public  List<Trend> queryTrend(){
        return bigdataMapper.selectTrend();
    }


}
