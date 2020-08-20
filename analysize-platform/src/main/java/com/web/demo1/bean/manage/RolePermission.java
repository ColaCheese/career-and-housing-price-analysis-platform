package com.web.demo1.bean.manage;/*
 * Welcome to use the TableGo Tools.
 * 
 * http://vipbooks.iteye.com
 * http://blog.csdn.net/vipbooks
 * http://www.cnblogs.com/vipbooks
 * 
 * Author:bianj
 * Email:edinsker@163.com
 * Version:4.1.2
 */

/**
 * (ROLEPERMISSION)
 * 
 * @author bianj
 * @version 1.0.0 2019-08-15
 */
public class RolePermission implements java.io.Serializable {
    /** 版本号 */
    private static final long serialVersionUID = -5409464748947488082L;

    private Long roleID;

    private String menuUrl;

    private String roleName;

    private Long menuID;

    public Long getRoleID() {
        return roleID;
    }

    public void setRoleID(Long roleID) {
        this.roleID = roleID;
    }

    public String getMenuUrl() {
        return menuUrl;
    }

    public void setMenuUrl(String menuUrl) {
        this.menuUrl = menuUrl;
    }

    public String getRoleName() {
        return roleName;
    }

    public void setRoleName(String roleName) {
        this.roleName = roleName;
    }

    public Long getMenuID() {
        return menuID;
    }

    public void setMenuID(Long menuID) {
        this.menuID = menuID;
    }
}