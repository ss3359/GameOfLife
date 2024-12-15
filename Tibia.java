/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author owner
 */
import java.util.Scanner;
import java.util.Random;
import javax.swing.*;
import java.io.Reader;
import java.io.Writer;
import java.math.*;
import javax.lang.model.SourceVersion;

class GameOfLife {

    private static int rows, columns, generations;
    private static boolean grid[][];

    public GameOfLife(int r, int c, int g) {
        this.rows = r;
        this.columns = c;
        this.generations = g;
        this.grid = new boolean[rows][columns];
        FillGrid(grid);
    }

    public static void FillGrid(boolean grid[][]) {
        Random r = new Random();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                grid[i][j] = r.nextBoolean();
            }
        }
    }

    public static boolean[][] GetGrid() {
        return grid;
    }

    public static int GetGenerations() {
        return generations;
    }

    public static void PrintGrid(boolean grid[][]) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (grid[i][j] == true) {
                    System.out.print("1" + " ");
                } else {
                    System.out.print("0" + " ");
                }
            }
            System.out.println();
        }
    }

    public static boolean[][] DoAlgorithm(boolean grid[][], int x, int y) {

        int alive = 0;
        boolean NewGrid[][]=new boolean[rows][columns];

        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                if (dx == 0 && dy == 0) {
                    continue;
                }
                int nx= x+dx, ny=y+dy; 
                if ((nx>=0&& nx<rows)&&(ny>=0 &&ny<columns)) {
                    if (grid[nx][ny] == true) {
                        alive++;
                    } 

                }

            }
        }

        if (grid[x][y] == true &&(alive < 2 ||alive >3)) {
            NewGrid[x][y] = false;
        } else if (grid[x][y] == true && (alive == 2||alive==3)) {
            NewGrid[x][y] = true;
        } else if (grid[x][y] == false && alive==3) {
            NewGrid[x][y] = true;
        }
        else{
            NewGrid[x][y]=grid[x][y];
        }
       return NewGrid;
    }

    public static void Generations(boolean[][] grid) {
        for (int n = 0; n < generations; n++) {
            boolean NewGrid[][] = new boolean[rows][columns];
            
            for (int x = 0; x < rows; x++) {
                for (int y = 0; y < columns; y++) {
                    NewGrid[x][y]=DoAlgorithm(grid, x, y)[x][y];
                }
            }
            grid=NewGrid;
            PrintGrid(grid);
            System.out.println();
        }

    }
}

public class Tibia {

    public static void main(String args[]) {

        GameOfLife g = new GameOfLife(25, 25,10);
        
        boolean[][] start=g.GetGrid(); 
        g.Generations(start);

    }
}
