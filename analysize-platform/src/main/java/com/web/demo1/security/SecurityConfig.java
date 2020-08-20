package com.web.demo1.security;

import com.web.demo1.service.serviceImpl.MyUserDetailsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.util.DigestUtils;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private MyUserDetailsService userService;


    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {

        //校验用户
        auth.userDetailsService( userService ).passwordEncoder( new PasswordEncoder() {
            //对密码进行加密
            @Override
            public String encode(CharSequence charSequence) {
                System.out.println(charSequence.toString());
                return DigestUtils.md5DigestAsHex(charSequence.toString().getBytes());
            }
            //对密码进行判断匹配
            @Override
            public boolean matches(CharSequence charSequence, String s) {
                String encode = DigestUtils.md5DigestAsHex(charSequence.toString().getBytes());
                boolean res = s.equals( encode );
                return res;
            }
        } );

    }
    @Override
    public void configure(WebSecurity web) throws Exception {
        // 设置不拦截规则
        web.ignoring().antMatchers("/reg","/layuiadmin/**","/forget","/ifreg","/toreg");

    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable();
        http.authorizeRequests()
                .antMatchers("/","/login","/login-error","/401","/css/**","/js/**").permitAll()
                .antMatchers("/menuController/**").authenticated()
                .anyRequest().authenticated()
                .and()
                .formLogin().loginPage( "/login" ).loginProcessingUrl("/user/login").successForwardUrl("/").failureUrl( "/login-error" )
                .and()
                .exceptionHandling().accessDeniedPage( "/401" )
                .and()
                .headers().frameOptions().sameOrigin();
        http.logout().logoutSuccessUrl( "/login" );
    }


}
