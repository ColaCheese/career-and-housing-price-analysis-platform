package com.web.demo1.service.serviceImpl;

import com.web.demo1.bean.manage.Role;
import com.web.demo1.bean.user.User;
import com.web.demo1.dao.UserMapper;
import com.web.demo1.dao.roleMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class MyUserDetailsService implements UserDetailsService {

    @Autowired
    private UserMapper userMapper;
    @Autowired
    private roleMapper rolemapper;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        //查数据库
        User user = userMapper.loadUserByUsername( username );
        if (null != user) {
            List<String> roleIDs = userMapper.getRoleID(user.getUserID().toString());
            List<Role> roles = new ArrayList<>();
            for (String id : roleIDs){
                Role role = rolemapper.getRolec(id);
                roles.add(role);
            }
            user.setAuthorities( roles );
        }
        else {
            user = new User();
            user.setUsername(username);
            user.setPassword("null");
        }
        System.out.println("uuuuuuuuuuuuuuuuuuu:"+user);
        return user;
    }


}
