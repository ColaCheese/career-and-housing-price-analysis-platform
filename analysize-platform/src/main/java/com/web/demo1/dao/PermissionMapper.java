package com.web.demo1.dao;

import com.web.demo1.bean.manage.RolePermission;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface PermissionMapper {
    @Select("select * from roleMenu")
    public List<RolePermission> getRolePermissions();


}
