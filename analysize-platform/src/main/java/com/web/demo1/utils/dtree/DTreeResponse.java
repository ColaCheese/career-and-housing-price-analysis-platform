package com.web.demo1.utils.dtree;

/** response返回类*/
public class DTreeResponse {
    /** 状态码*/
    private int code;
    /** 信息标识*/
    private String msg;
    /** 状态类*/
    private Status status;
    /** 数据*/
    private Object data;

    //省略了get、set、toString方法

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    public Status getStatus() {
        return status;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    public Object getData() {
        return data;
    }

    public void setData(Object data) {
        this.data = data;
    }
}

