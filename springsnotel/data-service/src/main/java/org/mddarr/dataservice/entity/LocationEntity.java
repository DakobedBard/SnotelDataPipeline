package org.mddarr.dataservice.entity;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "locations" )
public class LocationEntity {
    @Id
    private Integer location_id;
    private String location_name;
    private Integer elevation;
    private Integer region_id;

    public Integer getLocation_id() {
        return location_id;
    }

    public void setLocation_id(Integer location_id) {
        this.location_id = location_id;
    }

    public String getLocation_name() {
        return location_name;
    }

    public void setLocation_name(String location_name) {
        this.location_name = location_name;
    }

    public Integer getElevation() {
        return elevation;
    }

    public void setElevation(Integer elevation) {
        this.elevation = elevation;
    }

    public Integer getRegion_id() {
        return region_id;
    }

    public void setRegion_id(Integer region_id) {
        this.region_id = region_id;
    }
    public LocationEntity(){}

    public LocationEntity(Integer location_id, String location_name, Integer elevation, Integer region_id) {
        this.location_id = location_id;
        this.location_name = location_name;
        this.elevation = elevation;
        this.region_id = region_id;
    }
}
