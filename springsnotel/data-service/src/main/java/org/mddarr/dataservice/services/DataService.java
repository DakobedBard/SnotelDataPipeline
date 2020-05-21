package org.mddarr.dataservice.services;

import org.mddarr.dataservice.dao.LocationRepository;
import org.mddarr.dataservice.entity.LocationDataEntity;
import org.mddarr.dataservice.entity.LocationEntity;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class DataService {

    @Autowired
    private LocationRepository locationRepository;

    public List<LocationEntity> getLocations() {
        List<LocationEntity> locations = new ArrayList<>();
        locationRepository.findAll().forEach(locations::add);
        System.out.println("The number of locationis " + locations.size());
        LocationEntity l = locations.get(0);
        System.out.println("The first location is " +  l.getLocation_name());
        return locations;
    }



//    public Optional<LocationDataEntity> getLocation(Integer id){
//        return locationRepository.findById(id);
//    }




}
