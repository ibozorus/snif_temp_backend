package com.example.temp_backend.repository;

import com.example.temp_backend.model.Hersteller;
import com.example.temp_backend.model.Temperature;
import com.example.temp_backend.model.User;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import java.util.Optional;

public interface UserRepository extends CrudRepository<User, Long> {

    @Query("SELECT a FROM User a WHERE a.username = ?1")
    User findUserByUsername(String userName);
}
