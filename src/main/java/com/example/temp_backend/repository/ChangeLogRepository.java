package com.example.temp_backend.repository;

import com.example.temp_backend.model.ChangeLog;
import org.springframework.data.repository.CrudRepository;

public interface ChangeLogRepository extends CrudRepository<ChangeLog, Long> {
}
