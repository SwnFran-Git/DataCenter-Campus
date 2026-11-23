USE SERVERDB;

DELIMITER $$

-- Registrar servidor

CREATE PROCEDURE sp_RegistrarServidor(
    IN p_rack INT,
    IN p_temperatura DECIMAL(10,2),
    IN p_consumo DECIMAL(10,2),
    IN p_mensaje_alerta VARCHAR(100)
)
BEGIN
    INSERT INTO NodoServidor (rack, Temperatura, Consumo, Mensaje_alerta)
    VALUES (p_rack, p_temperatura, p_consumo, p_mensaje_alerta);
END $$


-- Listar servidores

CREATE PROCEDURE sp_listarServidores()
BEGIN
    SELECT rack, Temperatura, Consumo, Mensaje_alerta
    FROM NodoServidor;
END $$


-- Buscar servidores

CREATE PROCEDURE sp_Busqueda_Servers(
    IN p_criterio VARCHAR(100)
)
BEGIN
    SELECT * FROM NodoServidor
    WHERE rack LIKE CONCAT('%', p_criterio, '%')
       OR Mensaje_alerta LIKE CONCAT('%', p_criterio, '%');
END $$

DELIMITER ;