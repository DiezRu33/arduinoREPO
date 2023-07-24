#include <Servo.h>

// Define los pines a los que están conectados los servomotores
const int pinHombro = 9;
const int pinCodo = 10;
const int pinPinza = 11;

// Crea objetos servo para controlar cada servomotor
Servo servoHombro;
Servo servoCodo;
Servo servoPinza;

// Ángulos iniciales de cada articulación
int anguloHombro = 90;
int anguloCodo = 90;
int anguloPinza = 0;

// Función para mover el brazo a una posición específica
void moverBrazo(int angHombro, int angCodo, int angPinza) {
  servoHombro.write(angHombro);
  servoCodo.write(angCodo);
  servoPinza.write(angPinza);
  delay(500); // Pequeño retardo para dar tiempo a que se mueva el servo
}

void setup() {
  // Inicializa los objetos servo
  servoHombro.attach(pinHombro);
  servoCodo.attach(pinCodo);
  servoPinza.attach(pinPinza);

  // Mueve el brazo a la posición inicial
  moverBrazo(anguloHombro, anguloCodo, anguloPinza);
}

void loop() {
  // Ejemplo de movimiento del brazo robótico
  // Puedes modificar estos ángulos para adaptarlos a tu brazo robótico

  // Mueve el brazo hacia arriba
  moverBrazo(120, 45, 0);
  delay(1000);

  // Cierra la pinza
  moverBrazo(120, 45, 90);
  delay(1000);

  // Mueve el brazo hacia abajo
  moverBrazo(90, 90, 90);
  delay(1000);

  // Abre la pinza
  moverBrazo(90, 90, 0);
  delay(1000);
}
