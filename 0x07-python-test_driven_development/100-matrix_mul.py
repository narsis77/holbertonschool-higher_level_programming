#!/usr/bin/python3
"""Module that contains a function to divide a matrix by a scalar"""


def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    if len(m_b) < 1:
        raise ValueError("m_b can't be empty")
    arowlen = len(m_a[0])
    if arowlen != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for row in m_a:
        if len(row) != arowlen:
            raise TypeError("each row of m_a must should be of the same size")
        for col in row:
            if type(col) is not float and type(col) is not int:
                raise TypeError("m_a should contain only integers or floats")
    browlen = len(m_b[0])
    for row in m_b:
        if len(row) != browlen:
            raise TypeError("each row of m_b must should be of the same size")
        for col in row:
            if type(col) is not float and type(col) is not int:
                raise TypeError("m_b should contain only integers or floats")
    newmatrix = []
    for x in range(len(m_a)):
        newrow = []
        for y in range(browlen):
            sum = 0
            for z in range(arowlen):
                sum += m_a[x][z] * m_b[z][y]
            newrow.append(sum)
        newmatrix.append(newrow)
    return newmatrix
