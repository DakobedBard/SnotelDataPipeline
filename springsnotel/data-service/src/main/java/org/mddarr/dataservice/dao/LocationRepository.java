package org.mddarr.dataservice.dao;

import org.mddarr.dataservice.entity.LocationEntity;
import org.springframework.data.repository.CrudRepository;

public interface LocationRepository extends CrudRepository<LocationEntity, Integer> {
}
