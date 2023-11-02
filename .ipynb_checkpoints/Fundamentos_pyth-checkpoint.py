{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cd9f4534",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ingrese su dirección de correo electrónico: steph\n",
      "La dirección de correo electrónico no es válida.\n"
     ]
    }
   ],
   "source": [
    "def es_direccion_valida(email):\n",
    "    if \"@\" in email:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "direccion_email = input(\"Ingrese su dirección de correo electrónico: \")\n",
    "if es_direccion_valida(direccion_email):\n",
    "    print(\"La dirección de correo electrónico es válida.\")\n",
    "else:\n",
    "    print(\"La dirección de correo electrónico no es válida.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6f1ff7d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ingrese un numero: 13\n",
      "el numero no es primo.\n"
     ]
    }
   ],
   "source": [
    "def es_primo(numero):\n",
    "    if numero % 2 == 0:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "44548ce7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ingrese un número entero (0 para salir): 34\n",
      "El factorial de 34 es 295232799039604140847618609643520000000\n",
      "Ingrese un número entero (0 para salir): 0\n",
      "Total de números leídos: 1\n"
     ]
    }
   ],
   "source": [
    "def factorial(numero):\n",
    "    if numero == 0:\n",
    "        return 1\n",
    "    else:\n",
    "        return numero * factorial(numero - 1)\n",
    "\n",
    "total_numeros = 0\n",
    "while True:\n",
    "    try:\n",
    "        numero = int(input(\"Ingrese un número entero (0 para salir): \"))\n",
    "        if numero == 0:\n",
    "            break\n",
    "        total_numeros += 1\n",
    "        print(f\"El factorial de {numero} es {factorial(numero)}\")\n",
    "    except ValueError:\n",
    "        print(\"Entrada no válida. Introduzca un número entero válido.\")\n",
    "\n",
    "print(f\"Total de números leídos: {total_numeros}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9bb3a07d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entroduzca un numero: 13\n",
      "Numero: 13\n",
      "Factorial: 6227020800\n",
      "Cantidad de dígitos en el factorial: 10\n"
     ]
    }
   ],
   "source": [
    "def factorial(numero):\n",
    "    if numero == 0:\n",
    "        return 1\n",
    "    else:\n",
    "        return numero * factorial(numero - 1)\n",
    "\n",
    "def num(numero):\n",
    "    return len(str(numero))\n",
    "\n",
    "numero = int(input(\"Entroduzca un numero: \"))\n",
    "resultado = factorial(numero)\n",
    "cantidad_digitos = num(resultado)\n",
    "\n",
    "print(f\"Numero: {numero}\")\n",
    "print(f\"Factorial: {resultado}\")\n",
    "print(f\"Cantidad de dígitos en el factorial: {cantidad_digitos}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a24f51f1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
