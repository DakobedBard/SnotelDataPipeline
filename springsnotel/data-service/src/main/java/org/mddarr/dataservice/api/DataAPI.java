package org.mddarr.dataservice.api;

import org.mddarr.dataservice.entity.LocationEntity;
import org.mddarr.dataservice.services.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.List;


@RestController
@RequestMapping(value = "/locations/")
public class DataAPI {

    @Autowired
    private DataService dataService;

    @GetMapping()
    public String get() throws IOException {
        return "hello";
    }


    @GetMapping(value = "/get")
    public List<LocationEntity> getLocations() throws IOException {
        return dataService.getLocations();
    }

}
