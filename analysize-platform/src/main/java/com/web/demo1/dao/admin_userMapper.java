package com.web.demo1.dao;

import com.web.demo1.bean.manage.Manage_user;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface admin_userMapper {

    @Select("select user.userName,role.roleID,role.roleName from user left JOIN role on user.roleID = role.roleID where user.roleID > 2")
    public List<Manage_user> getuser();
    @Select("select user.userName,role.roleID,role.roleName from user left JOIN role on user.roleID = role.roleID where user.roleID > 2 limit #{start},#{pagesize}")
    public List<Manage_user> getuserbypage(@Param("start") int start,@Param("pagesize") int pagesize);
    @Delete("delete from user where userName = #{userName}")
    public int deleteuser(@Param("userName") String name);
    @Update("update user set roleID = #{roleID} where userName = #{userName}")
    public int updateuser(@Param("roleID") String ID,@Param("userName") String name);
    /////////////////////////////////////////////////////////////////
    @Select("select user.userName,user.password,role.roleName from user left JOIN role on user.roleID = role.roleID where user.roleID = 1")
    public List<Manage_user> getadmin();
    @Select("select user.userName,user.password,role.roleName from user left JOIN role on user.roleID = role.roleID where user.roleID = 1 limit #{start},#{pagesize}")
    public List<Manage_user> getadminbypage(@Param("start") int start,@Param("pagesize") int pagesize);
    @Delete("delete from user where userName = #{userName}")
    public int deleteadmin(@Param("userName") String name);
    @Update("update user set password = #{password} where userName = #{userName}")
    public int updateadmin(@Param("password") String password,@Param("userName") String name);
    @Insert("insert into user (userName,roleID,password,mail) VALUES (#{name},1,#{password},null)")
    public int insertadmin(@Param("name") String name,@Param("password") String password);
    @Select("select password from user where userName = #{userName}")
    public String getAdminpassword(String userName);
}
