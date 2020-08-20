package com.web.demo1.dao;

import com.web.demo1.bean.user.User;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface UserMapper {
    @Select("select userID,username,password from user where username = #{username}")
    public User loadUserByUsername(String username);

    @Select("select username from user where username = #{username}")
    public String getUsername(String username);

    @Select("select userID from user where username = #{username}")
    public String getUserID(String username);

    @Select("select roleID from user where userID = #{usrID}")
    public List<String> getRoleID(String userID);

    @Insert("insert into user values(null,#{user.username},#{user.password},#{user.mail},'3')")
    public void addUser(@Param(value = "user") User user);

}
