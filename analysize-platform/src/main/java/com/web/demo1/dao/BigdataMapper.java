package com.web.demo1.dao;

import com.web.demo1.bean.city.*;
import com.web.demo1.bean.district.*;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface BigdataMapper {
    //sql操作具体实现
    @Select("select * from citySold join cityRent join cityTrend on citySold.cityName=cityRent.cityName and cityRent.cityName=cityTrend.cityName")
    public List<City> selectCityRent();

    @Select("select areaName,cityName,areaRentprice from areaRent")
    public List<Area> selectAreaRent();

    @Select("select * from areaSold")
    public List<Area> selectCitySold();

    @Select("select * from districtSold")
    public List<District> selectDsold();

    @Select("select * from districtRent")
    public List<District> selectDrent();

    @Select("select * from trend")
    public  List<Trend> selectTrend();
}
