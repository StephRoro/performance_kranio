
/*******************************************Variables y Tipos de Datos*************************************************/

/*
Variables para almacenar valor. Hay 3 tipos de variables que son const let y var.
Tipos de datos tenemos Numericos (Number, BigInt), String, Booleanos, Null, Undefinided
var para declarar una variable
let se declara en un bloque de codigo especifico
const se declara en un bloque de codigo especifico y es un valor constante (que mo puede cambiar)
*/

/*
Mostrar el promedio de notas de un alumno:
*/


const notas = [85, 90, 78, 92, 88];
const sumaNotas = notas.reduce((total, nota) => total + nota, 0);
const promedio = sumaNotas / notas.length;
console.log(`El promedio de notas es: ${promedio}`);


/*
Calcular el porcentaje que debe pagar un cliente en la compra 
de una motocicleta a plazos en un período de 6 meses, con un interés mensual progresivo del 3.5%:
*/


const costoMotocicleta = 1000;
const tasaInteresMensual = 0.035;
const meses = 6;
let saldoPendiente = costoMotocicleta;
let porcentajeTotal = 0;

for (let i = 0; i < meses; i++) {
  saldoPendiente += tasaInteresMensual * saldoPendiente;
}

porcentajeTotal = (saldoPendiente / costoMotocicleta)*100
console.log(`El cliente debe pagar un ${porcentajeTotal.toFixed(2)}% del costo total de la motocicleta.`);



/*******************************************Operadores y Expresiones*************************************************/

/*
un operador es un simbolo que define el tipo de operacion que vamos a efectuar.EXpresiones son secuencias de operadores.
Sirven para realizar calculos, comparar valores, asignar valores, conctenar etc.
+, -, *, /, ==, !=, <, >, <=, >=, &&, ||, !, +=, -=, *=, /=, %=, etc
*/


/*
Un alumno tiene las siguientes notas en los exámenes: 5.25, 7.85, 3.4 Calcula cual es la media de este trimestre. 
A parte todos los alumnos reciben 1 punto mas a la media por un trabajo que hicieron, muestra por pantalla su nota final.
*/

const notes = [5.25, 7.85, 3.4];
const trabajo = 1;
const media = (notes.reduce((a, b) => a + b, 0) / notes.length) + trabajo;
console.log("La nota final del alumno es:", media);


/*
Haz que un programa resuelva la siguiente ecuación para los valores x= 2,4,6,8:  (7(3X+2)-5(4X-3) -1)/4.
*/
function resolverEcuacion(x) {
    return (7 * (3 * x + 2) - 5 * (4 * x - 3) - 1) / 4;
  }  
const valoresX = [2, 4, 6, 8];  
valoresX.forEach((x) => {
  const resultado = resolverEcuacion(x);
  console.log(`Para x=${x}, el resultado es: ${resultado}`);
});

/*
El perímetro de un rectángulo es de 252 metros y su base mide 6 metros mas que la altura, ¿Cuánto mide la base?.
Calcula que numero dividido entre 8 y el cual le sumas 12 sale 52.
*/

const perimetro = 252;
const altura = perimetro / 4 - (6/2); 
const base = altura + 6; 
const ver = 2*(base+altura)
console.log("La base del rectángulo mide:", base, "metros");
console.log("el perimetro del rectángulo mide:", ver, "metros");

/*
Calcula que numero dividido entre 8 y el cual le sumas 12 sale 52.
*/

const resultadoDeseado = 52;
const numero = (resultadoDeseado - 12) * 8;
console.log("El número buscado es:", numero);


/*******************************************Operadores y Expresiones*************************************************/

/*
Las estructuras de control en Java son construcciones de programación  que se utilizan para controlar y ordenar el flujo de ejecución de un programa.
Sirven para tomar decisiones, repetir tareas, agrupar instrucciones:
Tienes estructuras de decision (if, else if, else)
estructuras de repeticion (for, while)
estructuras de control de salto (break)
*/

/*Diseñe un algoritmo que determine si un número es o no es, par positivo.*/
function esParPositivo(numero) {
    if (numero > 0 && numero % 2 === 0) {
        return "Es par positivo";
    } else {
        return "No es par positivo";
    }
}

const num = 6; 
console.log(esParPositivo(num));

/*Escribir una programa que pida la nota de un examen (un número real entre 0 y 10) e 
imprima por pantalla la calificación en formato “Reprueba”, si la nota es menor que  5, 
“Aprobado” si esta entre 5 y 7 sin incluirlo, “Notable” si esta entre 7 y 9 sin incluirlo,  
“Sobresaliente” si esta entre 9 y 10 sin incluirlo y “Excelente”  si la nota es igual a 10
.*/

function obtenerCalificacion(nota) {
    if (nota < 5) {
        return "Reprueba";
    } else if (nota >= 5 && nota < 7) {
        return "Aprobado";
    } else if (nota >= 7 && nota < 9) {
        return "Notable";
    } else if (nota >= 9 && nota < 10) {
        return "Sobresaliente";
    } else if (nota === 10) {
        return "Excelente";
    } else {
        return "Nota fuera de rango";
    }
}
const notaExamen = 8; 
console.log("Calificación:", obtenerCalificacion(notaExamen));


/*Dado un número entero determine la cantidad de dígitos que tiene.*/

function contarDigitos(numero) {
    const numeroAbsoluto = Math.abs(numero); 
    return numeroAbsoluto.toString().length;
}
const numeroEntero = -12345;
console.log("Cantidad de dígitos:", contarDigitos(numeroEntero));


/*Dado un número entero determine  la suma de sus dígitos*/

function sumaDigitos(numero) {
    const numeroAbsoluto = Math.abs(numero);
    const digitos = numeroAbsoluto.toString().split("").map(Number);
    const suma = digitos.reduce((total, digito) => total + digito, 0);
    return suma;
}

const numeroEntero2 = 12345;
console.log("Suma de dígitos:", sumaDigitos(numeroEntero2));
