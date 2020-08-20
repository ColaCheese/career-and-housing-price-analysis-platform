package com.web.demo1.service.serviceImpl;

import com.web.demo1.bean.manage.RolePermission;
import com.web.demo1.dao.PermissionMapper;
import com.web.demo1.dao.roleMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.ConfigAttribute;
import org.springframework.security.access.SecurityConfig;
import org.springframework.security.web.FilterInvocation;
import org.springframework.security.web.access.intercept.FilterInvocationSecurityMetadataSource;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.stereotype.Component;

import javax.servlet.http.HttpServletRequest;
import java.util.*;

@Component
public class MyInvocationSecurityMetadataSourceService implements FilterInvocationSecurityMetadataSource {

    @Autowired
    private PermissionMapper permissionMapper;
    @Autowired
    private roleMapper rolemapper;
    @Autowired
    private com.web.demo1.dao.menuMapper menuMapper;

    /**
     * 每一个资源所需要的角色 Collection<ConfigAttribute>决策器会用到
     */
    private static HashMap<String, Collection<ConfigAttribute>> map =null;


    /**
     * 返回请求的资源需要的角色
     */
    @Override
    public Collection<ConfigAttribute> getAttributes(Object o) throws IllegalArgumentException {
        if (null == map) {
            loadResourceDefine();
        }
        //object 中包含用户请求的request 信息
        HttpServletRequest request = ((FilterInvocation) o).getHttpRequest();
        //System.out.println("有问题："+request.getRequestURI());
        //System.out.println("Request请求："+request.getRequestURI());
        for (Iterator<String> it = map.keySet().iterator(); it.hasNext();) {
            String url = it.next();
            if (new AntPathRequestMatcher( url ).matches( request )) {
                //System.out.println("输出对应url的map值："+ map.get( url ));
                return map.get( url );
            }
            /*System.out.println("map里的"+url);
            System.out.println("请求里的"+request.getRequestURI());
            if(url.equals(request.getRequestURI()))
                return map.get( url );*/
        }
        //System.out.println("getAttributes输出null");
        return null;
    }

    @Override
    public Collection<ConfigAttribute> getAllConfigAttributes() {
        return null;
    }

    @Override
    public boolean supports(Class<?> aClass) {
        return true;
    }

    /**
     * 初始化 所有资源 对应的角色
     */
    public void loadResourceDefine() {
        map = new HashMap<>(16);
        //权限资源 和 角色对应的表  也就是 角色权限 中间表
        List<RolePermission> rolePermissions = permissionMapper.getRolePermissions();

        //某个资源 可以被哪些角色访问
        for (RolePermission rolePermission : rolePermissions) {

            String url = menuMapper.getMenuUrl(rolePermission.getMenuID().toString());
            String roleName = rolemapper.getRoleName(rolePermission.getRoleID().toString());
            ConfigAttribute role = new SecurityConfig(roleName);

            if(map.containsKey(url)){
                map.get(url).add(role);
            }else{
                List<ConfigAttribute> list =  new ArrayList<>();
                list.add( role );
                map.put( url , list );
            }
        }
        System.out.println("所有url角色权限："+map);
    }


}
