package com.web.demo1.bean.city;

public class Data {
    private String analysisID;
    private String percent;//首付比
    private String years;//贷款年限
    private String rate;//利率

    public String getAnalysisID() {
        return analysisID;
    }

    public void setAnalysisID(String analysisID) {
        this.analysisID = analysisID;
    }

    public String getPercent() {
        return percent;
    }

    public void setPercent(String percent) {
        this.percent = percent;
    }

    public String getYears() {
        return years;
    }

    public void setYears(String years) {
        this.years = years;
    }

    public String getRate() {
        return rate;
    }

    public void setRate(String rate) {
        this.rate = rate;
    }
}
