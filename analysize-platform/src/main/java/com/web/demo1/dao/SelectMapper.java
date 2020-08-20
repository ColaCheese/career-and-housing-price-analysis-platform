package com.web.demo1.dao;

import com.web.demo1.bean.city.Analysis;
import com.web.demo1.bean.city.Data;
import com.web.demo1.bean.city.Trend;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface SelectMapper {

    @Select("select cityName from citySold")
    public List<String> getAllcity();

    @Select("select distinct trendName from trend ")
    public List<String> getAllTrend();

    @Select("select * from analysis")
    public List<Data> getAllAna();

    @Select("select * from analysis where analysisID = #{analysisID}")
    public Data getOneAna(String analysisID);

    @Select("select citySoldPrice,citySoldNum from citySold where cityName = #{cityName}")
    public Analysis getAnaSold(String cityName);

    @Select("select cityRentPrice,cityRentNum from cityRent where cityName = #{cityName}")
    public Analysis getAnaRent(String cityName);

    @Select("select trendPrice,trendNum from trend where cityName = #{cityName} and trendName = #{trendName}")
    public Trend getAnaTrend(@Param("cityName") String cityName, @Param("trendName") String trendName);


}
