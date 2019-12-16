import time
from enum import Enum

from computer import Computer

codes = [1, 380, 379, 385, 1008, 2655, 990435, 381, 1005, 381, 12, 99, 109, 2656, 1101, 0, 0, 383, 1102, 1, 0, 382,
         21002, 382, 1, 1, 21001, 383, 0, 2, 21102, 1, 37, 0, 1105, 1, 578, 4, 382, 4, 383, 204, 1, 1001, 382, 1, 382,
         1007, 382, 42, 381, 1005, 381, 22, 1001, 383, 1, 383, 1007, 383, 24, 381, 1005, 381, 18, 1006, 385, 69, 99,
         104, -1, 104, 0, 4, 386, 3, 384, 1007, 384, 0, 381, 1005, 381, 94, 107, 0, 384, 381, 1005, 381, 108, 1106, 0,
         161, 107, 1, 392, 381, 1006, 381, 161, 1101, 0, -1, 384, 1106, 0, 119, 1007, 392, 40, 381, 1006, 381, 161,
         1101, 1, 0, 384, 21002, 392, 1, 1, 21101, 22, 0, 2, 21102, 0, 1, 3, 21102, 138, 1, 0, 1106, 0, 549, 1, 392,
         384, 392, 20102, 1, 392, 1, 21101, 22, 0, 2, 21102, 3, 1, 3, 21101, 161, 0, 0, 1105, 1, 549, 1101, 0, 0, 384,
         20001, 388, 390, 1, 20102, 1, 389, 2, 21101, 180, 0, 0, 1105, 1, 578, 1206, 1, 213, 1208, 1, 2, 381, 1006, 381,
         205, 20001, 388, 390, 1, 20102, 1, 389, 2, 21102, 1, 205, 0, 1105, 1, 393, 1002, 390, -1, 390, 1101, 1, 0, 384,
         20101, 0, 388, 1, 20001, 389, 391, 2, 21101, 228, 0, 0, 1106, 0, 578, 1206, 1, 261, 1208, 1, 2, 381, 1006, 381,
         253, 20101, 0, 388, 1, 20001, 389, 391, 2, 21102, 1, 253, 0, 1105, 1, 393, 1002, 391, -1, 391, 1102, 1, 1, 384,
         1005, 384, 161, 20001, 388, 390, 1, 20001, 389, 391, 2, 21102, 279, 1, 0, 1105, 1, 578, 1206, 1, 316, 1208, 1,
         2, 381, 1006, 381, 304, 20001, 388, 390, 1, 20001, 389, 391, 2, 21102, 304, 1, 0, 1106, 0, 393, 1002, 390, -1,
         390, 1002, 391, -1, 391, 1101, 1, 0, 384, 1005, 384, 161, 21001, 388, 0, 1, 20102, 1, 389, 2, 21102, 1, 0, 3,
         21102, 1, 338, 0, 1106, 0, 549, 1, 388, 390, 388, 1, 389, 391, 389, 20101, 0, 388, 1, 20102, 1, 389, 2, 21102,
         1, 4, 3, 21101, 365, 0, 0, 1106, 0, 549, 1007, 389, 23, 381, 1005, 381, 75, 104, -1, 104, 0, 104, 0, 99, 0, 1,
         0, 0, 0, 0, 0, 0, 273, 19, 19, 1, 1, 21, 109, 3, 22102, 1, -2, 1, 22101, 0, -1, 2, 21102, 1, 0, 3, 21102, 414,
         1, 0, 1105, 1, 549, 22101, 0, -2, 1, 21202, -1, 1, 2, 21101, 429, 0, 0, 1106, 0, 601, 2101, 0, 1, 435, 1, 386,
         0, 386, 104, -1, 104, 0, 4, 386, 1001, 387, -1, 387, 1005, 387, 451, 99, 109, -3, 2106, 0, 0, 109, 8, 22202,
         -7, -6, -3, 22201, -3, -5, -3, 21202, -4, 64, -2, 2207, -3, -2, 381, 1005, 381, 492, 21202, -2, -1, -1, 22201,
         -3, -1, -3, 2207, -3, -2, 381, 1006, 381, 481, 21202, -4, 8, -2, 2207, -3, -2, 381, 1005, 381, 518, 21202, -2,
         -1, -1, 22201, -3, -1, -3, 2207, -3, -2, 381, 1006, 381, 507, 2207, -3, -4, 381, 1005, 381, 540, 21202, -4, -1,
         -1, 22201, -3, -1, -3, 2207, -3, -4, 381, 1006, 381, 529, 22101, 0, -3, -7, 109, -8, 2106, 0, 0, 109, 4, 1202,
         -2, 42, 566, 201, -3, 566, 566, 101, 639, 566, 566, 1202, -1, 1, 0, 204, -3, 204, -2, 204, -1, 109, -4, 2106,
         0, 0, 109, 3, 1202, -1, 42, 594, 201, -2, 594, 594, 101, 639, 594, 594, 20101, 0, 0, -2, 109, -3, 2105, 1, 0,
         109, 3, 22102, 24, -2, 1, 22201, 1, -1, 1, 21101, 0, 509, 2, 21102, 646, 1, 3, 21101, 1008, 0, 4, 21102, 1,
         630, 0, 1105, 1, 456, 21201, 1, 1647, -2, 109, -3, 2106, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 0, 2,
         0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 1, 1,
         0, 0, 2, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2,
         0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0,
         0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 1, 1, 0, 0, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0,
         0, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 2, 0, 0,
         2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 1, 1, 0, 2, 2, 2, 0, 2, 0, 0, 0, 2, 2, 2,
         0, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 1, 1, 0, 2, 0, 2, 2, 2, 2,
         2, 2, 2, 0, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 1, 0, 2,
         2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 2, 2, 0, 0, 0, 2, 0, 0, 2,
         0, 1, 1, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0,
         2, 2, 2, 2, 0, 0, 1, 1, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0,
         0, 2, 0, 2, 2, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 2,
         2, 0, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
         0, 2, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 0, 0, 2, 0, 0, 2, 2, 0, 0, 1, 1, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2,
         0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 1, 1, 0, 2, 0, 2, 2, 0, 2, 0, 0,
         0, 0, 0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 1, 1, 0, 0, 2, 0,
         2, 2, 0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 0, 1,
         1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 36, 24, 85, 66,
         70, 87, 60, 26, 72, 78, 96, 17, 40, 97, 35, 47, 41, 13, 71, 87, 40, 95, 60, 61, 79, 41, 31, 4, 6, 72, 88, 63,
         33, 79, 38, 41, 34, 3, 11, 4, 27, 85, 37, 24, 77, 81, 5, 33, 59, 50, 51, 28, 42, 14, 69, 71, 14, 35, 13, 5, 20,
         29, 44, 78, 8, 18, 63, 26, 98, 35, 57, 68, 94, 68, 34, 81, 30, 41, 1, 27, 71, 55, 61, 57, 42, 61, 3, 11, 16,
         50, 42, 15, 53, 95, 17, 77, 60, 93, 39, 72, 17, 23, 8, 50, 14, 70, 65, 29, 79, 96, 23, 24, 31, 57, 83, 20, 58,
         77, 69, 59, 92, 75, 89, 27, 58, 33, 46, 64, 28, 15, 95, 50, 62, 11, 30, 65, 37, 81, 47, 55, 29, 75, 69, 83, 14,
         41, 31, 83, 71, 76, 4, 74, 88, 64, 94, 36, 63, 31, 72, 34, 7, 12, 49, 76, 8, 64, 18, 49, 74, 95, 18, 38, 32,
         96, 63, 36, 58, 38, 16, 79, 5, 17, 28, 80, 42, 49, 87, 19, 51, 27, 77, 70, 85, 78, 28, 24, 47, 87, 67, 72, 50,
         80, 47, 57, 83, 48, 18, 30, 10, 50, 36, 84, 90, 28, 73, 15, 97, 86, 79, 75, 31, 65, 3, 98, 13, 39, 90, 8, 38,
         69, 22, 32, 26, 87, 60, 47, 56, 79, 58, 46, 54, 24, 75, 37, 33, 58, 41, 67, 84, 42, 30, 59, 29, 3, 29, 88, 83,
         46, 16, 94, 48, 48, 72, 80, 5, 28, 16, 23, 47, 74, 91, 79, 80, 14, 34, 88, 83, 9, 88, 96, 15, 62, 79, 53, 27,
         10, 76, 98, 74, 27, 18, 75, 92, 73, 88, 92, 62, 39, 12, 34, 73, 86, 65, 50, 86, 36, 20, 46, 42, 65, 15, 63, 40,
         20, 45, 57, 38, 44, 89, 42, 8, 9, 24, 43, 96, 4, 87, 37, 46, 78, 29, 56, 70, 17, 76, 96, 12, 9, 37, 32, 59, 45,
         97, 19, 97, 46, 35, 19, 22, 28, 42, 54, 81, 67, 29, 57, 85, 18, 94, 45, 96, 87, 98, 15, 20, 2, 95, 15, 53, 15,
         33, 9, 69, 31, 3, 56, 9, 25, 41, 31, 43, 27, 54, 21, 89, 6, 37, 58, 52, 66, 11, 3, 21, 5, 41, 78, 79, 4, 13,
         77, 77, 70, 26, 12, 61, 58, 61, 93, 71, 53, 52, 67, 93, 6, 2, 18, 13, 94, 41, 22, 82, 61, 8, 96, 76, 92, 69,
         58, 41, 18, 13, 28, 46, 80, 62, 13, 51, 43, 90, 45, 7, 14, 75, 35, 68, 62, 54, 19, 67, 93, 35, 69, 97, 18, 58,
         37, 21, 21, 88, 92, 24, 40, 64, 83, 24, 74, 15, 52, 60, 71, 79, 53, 63, 85, 2, 53, 80, 95, 28, 51, 63, 5, 38,
         26, 18, 94, 60, 61, 88, 17, 41, 74, 27, 37, 15, 24, 91, 88, 13, 3, 55, 55, 18, 11, 32, 79, 19, 84, 42, 26, 46,
         10, 31, 47, 28, 68, 11, 15, 33, 61, 14, 40, 48, 49, 7, 40, 54, 61, 23, 82, 23, 4, 87, 56, 56, 16, 7, 28, 28, 2,
         21, 21, 51, 70, 81, 13, 63, 90, 17, 88, 89, 14, 77, 61, 69, 83, 71, 98, 59, 23, 40, 57, 46, 89, 10, 13, 66, 19,
         64, 22, 2, 25, 19, 49, 55, 70, 56, 92, 47, 64, 27, 16, 76, 68, 66, 90, 1, 88, 31, 20, 74, 68, 76, 47, 37, 83,
         94, 45, 67, 53, 33, 63, 27, 40, 10, 63, 23, 88, 32, 86, 37, 25, 52, 80, 70, 6, 45, 41, 84, 56, 11, 3, 59, 9,
         70, 6, 58, 94, 74, 67, 8, 27, 54, 80, 78, 37, 61, 52, 66, 24, 45, 55, 5, 66, 43, 54, 84, 61, 26, 6, 64, 92, 15,
         43, 75, 20, 32, 83, 56, 82, 44, 18, 76, 13, 11, 89, 4, 91, 20, 20, 88, 43, 96, 28, 73, 73, 57, 98, 29, 39, 45,
         73, 84, 36, 2, 47, 18, 36, 64, 38, 83, 54, 26, 21, 50, 37, 98, 3, 83, 90, 35, 19, 3, 27, 58, 49, 38, 2, 40, 19,
         18, 95, 41, 8, 47, 45, 8, 30, 55, 86, 96, 97, 48, 10, 59, 89, 46, 71, 86, 14, 94, 54, 25, 1, 2, 78, 29, 91, 65,
         51, 26, 2, 57, 27, 97, 9, 20, 1, 1, 47, 94, 18, 20, 57, 68, 24, 46, 8, 68, 98, 88, 88, 85, 76, 24, 82, 70, 86,
         35, 42, 87, 6, 73, 62, 95, 98, 6, 77, 60, 86, 89, 76, 57, 18, 29, 7, 90, 51, 54, 20, 28, 93, 60, 8, 25, 49, 28,
         7, 34, 6, 68, 79, 92, 10, 18, 55, 43, 85, 20, 47, 46, 15, 47, 80, 81, 46, 65, 47, 38, 2, 67, 92, 86, 54, 33,
         22, 71, 36, 3, 2, 71, 96, 36, 21, 70, 60, 58, 39, 71, 48, 74, 25, 94, 43, 44, 7, 55, 66, 87, 97, 53, 44, 72,
         47, 39, 94, 76, 45, 62, 57, 57, 48, 15, 82, 14, 60, 58, 32, 65, 42, 68, 27, 72, 35, 85, 14, 79, 61, 16, 85, 11,
         86, 35, 32, 13, 68, 70, 14, 13, 27, 47, 10, 26, 35, 60, 93, 10, 13, 75, 42, 77, 34, 59, 70, 5, 53, 62, 62, 91,
         57, 20, 96, 71, 61, 8, 57, 21, 45, 72, 44, 5, 23, 67, 64, 32, 97, 52, 78, 34, 26, 69, 76, 58, 69, 77, 71, 64,
         94, 10, 95, 71, 68, 15, 25, 42, 87, 78, 89, 58, 25, 11, 54, 75, 29, 74, 90, 89, 25, 90, 58, 98, 82, 5, 15, 35,
         49, 69, 68, 10, 23, 87, 87, 74, 46, 53, 22, 83, 84, 64, 5, 9, 68, 59, 54, 24, 22, 20, 61, 4, 2, 59, 84, 79, 77,
         72, 95, 80, 33, 12, 23, 3, 14, 23, 61, 18, 49, 32, 990435]

STRING = ''''''

TEST_STRING = ''''''
TEST_STRING2 = ''''''
TEST_STRING3 = ''''''


class DrawTile(Enum):
    EMPTY = ' '
    WALL = 'X'
    BLOCK = '$'
    PADDLE = '_'
    BALL = 'O'


class MapTile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


def run1():
    arcade = Computer(codes)
    arcade.program()
    tiles = [arcade.outputs[2 + 3 * i] for i in range(int(len(arcade.outputs) / 3))]
    return tiles.count(2)


class Game(object):
    def __init__(self):
        self.cpu = None
        self.paddle_pos = 0
        self.ball_pos = 0
        self.score = '0'
        self.num_blocks = 0
        self.map = None

    def move_joystick(self):
        if self.ball_pos > self.paddle_pos:
            return 1
        elif self.ball_pos < self.paddle_pos:
            return -1
        return 0

    def build_game(self, build_instructions):
        tmp = [[" "] * (50 + 1) for y_ in range(abs(24) + 1)]
        tmp[0][50] = str(self.score)
        tmp[0][49] = 'Score:'
        self.num_blocks = 0
        for x, y, draw in build_instructions:
            if x == -1 and y == 0:
                self.score = str(draw)
                continue

            if draw == MapTile.EMPTY.value:
                z = DrawTile.EMPTY.value
            elif draw == MapTile.WALL.value:
                z = DrawTile.WALL.value
            elif draw == MapTile.BLOCK.value:
                z = DrawTile.BLOCK.value
                self.num_blocks += 1
            elif draw == MapTile.PADDLE.value:
                z = DrawTile.PADDLE.value
                self.paddle_pos = x
            elif draw == MapTile.BALL.value:
                z = DrawTile.BALL.value
                self.ball_pos = x

            tmp[y][x] = z

        self.map = tmp

    def update_game(self, build_instructions):
        self.map[0][49] = 'Score:'
        for x, y, draw in build_instructions:
            if x == -1 and y == 0:
                self.score = str(draw)
                self.map[0][50] = str(self.score)
                continue

            if draw == MapTile.EMPTY.value:
                z = DrawTile.EMPTY.value
                if self.map[y][x] == '$':
                    self.num_blocks -= 1
            elif draw == MapTile.WALL.value:
                z = DrawTile.WALL.value
            elif draw == MapTile.BLOCK.value:
                z = DrawTile.BLOCK.value
            elif draw == MapTile.PADDLE.value:
                z = DrawTile.PADDLE.value
                self.paddle_pos = x
            elif draw == MapTile.BALL.value:
                z = DrawTile.BALL.value
                self.ball_pos = x

            self.map[y][x] = z
        self.map[0][50] = str(self.score)


clear = "\n" * 25


def run2():
    codes1 = codes.copy()
    codes1[0] = 2
    game = Game()
    game.cpu = Computer(codes1)

    while not game.cpu.halted:
        game.cpu.outputs = []
        game.cpu.program()
        instructions = game.cpu.outputs
        num_instrunctions = int(len(instructions) / 3)
        game_instructions = [instructions[3 * i:3 * (i + 1)] for i in range(num_instrunctions)]
        if game.map:
            game.update_game(game_instructions)
        else:
            game.build_game(game_instructions)

        dir = game.move_joystick()
        game.cpu.add_input(dir)

        # [print((" ".join(x))) for x in game.map]

    return game.score


if __name__ == "__main__":
    start_time = time.time()
    f = run1()
    g = run2()
    print(f"Part 1:", f)
    print(f"Part 2:", g)
    # [print((" ".join(x))) for x in g]

    print(time.time() - start_time)
