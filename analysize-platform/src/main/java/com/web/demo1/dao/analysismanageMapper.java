package com.web.demo1.dao;

import com.web.demo1.bean.city.Data;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface analysismanageMapper {

    @Select("select * from analysis")
    public List<Data> getData();
    @Select("select * from analysis limit #{start},#{pagesize}")
    public List<Data> getDatabypage(@Param("start") int start, @Param("pagesize") int pagesize);
    @Delete("delete from analysis where analysisID = #{ID}")
    public int deleteAnalysis(@Param("ID") String ID);
    @Update("update analysis set percent = #{percent}, years = #{years}, rate = #{rate} where analysisID = #{ID}")
    public int updateAnalysis(@Param("percent") String percent, @Param("years") String years, @Param("rate") String rate, @Param("ID") String ID);
    @Insert("insert into analysis (percent, years, rate) values (#{percent},#{years},#{rate})")
    public int addAnalyssis(@Param("percent") String percent, @Param("years") String years, @Param("rate") String rate);
    @Select("select LAST_INSERT_ID();")
    public int getnewId();
}
