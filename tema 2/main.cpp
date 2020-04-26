#include <iostream>
#include <fstream>
#include "splay_tree.h"

std::ifstream fin("abce.in");
std::ofstream fout("abce.out");

int main() {
    splay_tree sp;
    int q; int a, b1, b2;
    fin >> q;
    for (int i = 1; i <= q; ++i) {
        fin >> a;
        if (a == 1) {
            fin >> b1;
            sp.insereaza(b1);
        } else if (a == 2) {
            fin >> b1;
            sp.sterge(b1);
        } else if (a == 3) {
            fin >> b1;
            if (sp.cauta(b1)) fout << 1 << '\n';
            else fout << 0 << '\n';
        } else if (a == 4) {
            fin >> b1;
            fout << sp.pred(b1) << '\n';
        } else if (a == 5) {
            fin >> b1;
            fout << sp.succ(b1) << '\n';
        } else if (a == 6) {
            fin >> b1 >> b2;
            sp.interval(b1, b2);
        }

    }    return 0;
}
