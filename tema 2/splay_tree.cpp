//
// Created by Daria on 4/26/2020.
//

#include "splay_tree.h"
#include <iostream>

splay_tree::splay_tree() : radacina(nullptr), dimensiune(0) {}

void splay_tree::rotatie_stg(splay_tree::nod *x) {

    nod *y = x -> fdr;
    if (y) {
        x -> fdr = y -> fstg;
        if (y -> fstg) y -> fstg -> parinte = x;
        y -> parinte = x -> parinte;
    }

    if (!x -> parinte) radacina = y;
    else if (x == x-> parinte -> fstg) x -> parinte -> fstg = y;
    else x -> parinte -> fdr = y;
    if (y) y -> fstg = x;
    x -> parinte = y;

}

void splay_tree::rotatie_dr(splay_tree::nod *x) {

    nod *y = x -> fstg;
    if (y) {
        x -> fstg = y -> fdr;
        if (y -> fdr) y -> fdr -> parinte  = x;
        y -> parinte = x -> parinte;
    }

    if (!x -> parinte) radacina = y;
    else if (x == x -> parinte -> fstg) x -> parinte -> fstg = y;
    else x -> parinte -> fdr = y;
    if (y) y -> fdr = x;
    x -> parinte = y;
}

void splay_tree::splay(splay_tree::nod *x) {

    while (x -> parinte) {
        if (! x -> parinte -> parinte) {
            if (x -> parinte -> fstg == x) rotatie_dr( x->parinte );
            else rotatie_stg ( x -> parinte);
        } else if (x -> parinte -> fstg == x and
                   x -> parinte ->parinte -> fstg == x ->parinte) {
            rotatie_dr( x -> parinte -> parinte);
            rotatie_dr (x -> parinte);
        } else if (x -> parinte -> fdr == x and
                   x -> parinte -> parinte-> fdr == x -> parinte) {
            rotatie_stg( x-> parinte -> parinte);
            rotatie_stg(x -> parinte);
        } else if (x -> parinte -> fstg == x and
                   x -> parinte -> parinte -> fdr == x -> parinte) {
            rotatie_dr( x -> parinte);
            rotatie_stg (x -> parinte);
        } else {
            rotatie_stg( x -> parinte);
            rotatie_dr (x -> parinte);
        }
    }

}

void splay_tree::inlocuieste(splay_tree::nod *x, splay_tree::nod *y) {

    if (!x -> parinte) radacina = y;
    else if (x == x -> parinte -> fstg) x -> parinte -> fstg = y;
    else x -> parinte -> fdr = y;
    if (y) y -> parinte = x -> parinte;

}

void splay_tree::insereaza(const int &valoare) {

    nod *x = radacina;
    nod *y = nullptr;

    while (x) {
        y = x;
        if (x -> valoare < valoare) x = x -> fdr;
        else x = x -> fstg;
    }

    x = new nod(valoare);
    x -> parinte = y;
    if (!y) radacina = x;
    else if (y -> valoare < x -> valoare) y -> fdr = x;
    else y -> fstg = x;

    splay (x);
    dimensiune++;

}

splay_tree::nod *splay_tree::cauta(const int &valoare) {
    nod *x = radacina;
    while (x) {
        if (x -> valoare < valoare) x = x -> fdr;
        else if (valoare < x -> valoare) x = x -> fstg;
        else return x;
    }
    return nullptr;
}

void splay_tree::sterge(const int &valoare) {

    nod *x = cauta(valoare);
    if (!x) return;

    splay (x);

    if (!x -> fstg) inlocuieste(x, x-> fdr);
    else if (!x -> fdr) inlocuieste (x, x->fstg);
    else {
        nod *y = subarbore_min(x -> fdr);
        if (y -> parinte != x) {
            inlocuieste (y, y -> fdr);
            y -> fdr = x -> fdr;
            y -> fdr -> parinte = y;
        }
        inlocuieste (x, y);
        y -> fstg = x -> fstg;
        y -> fstg -> parinte = y;
    }

    delete x;
    dimensiune--;

}

/*const int &splay_tree::minim() {
    return subarbore_min(radacina) -> valoare;
}

const int &splay_tree::maxim() {
    return subarbore_max(radacina) -> valoare;
}*/

splay_tree::nod *splay_tree::subarbore_min(splay_tree::nod *x) {
    while (x -> fstg) x = x -> fstg;
    return x;
}
/*
splay_tree::nod *splay_tree::subarbore_max(splay_tree::nod *x) {
    while (x -> fdr) x = x -> fdr;
    return x;
}*/

/*
bool splay_tree::empty() const {
    return radacina == nullptr;
}
*/

/*
unsigned long splay_tree::dimensiune_arbore() const {
    return dimensiune;
}
*/

int splay_tree::pred(const int &valoare) {

    nod *x = radacina;
/*    int m = x -> valoare;
    while (x) {
        if (x -> valoare <= valoare) {
            m = x -> valoare;
            x = x -> fdr;
        } else {
            x = x -> fstg;
        }
    }
    return m;*/
    nod *p = nullptr;
    while (x) {
        if (x -> valoare <= valoare) {
            p = x;
            x = x -> fdr;
        }
        else {
            x = x -> fstg;
        }
    }

    if (p) return p -> valoare;
    return -1;
/*
    nod *x = cauta (valoare);
    //mergea doar daca in dadeam sa caute o valoare care se afla deja in arbore
    if (x -> fstg) return subarbore_max(x -> fstg) -> valoare;
    while (x -> parinte -> fstg == x) {x = x -> parinte;}
    return x -> parinte -> valoare;
*/

}

int splay_tree::succ(const int &valoare) {

    nod *x = radacina;
/*    int m = x -> valoare;
    while (x) {
        if (x -> valoare >= valoare) {
            m = x -> valoare;
            x = x -> fstg;
        } else {
            x = x -> fdr;
        }
    }
    return m;*/
    nod *p = nullptr;
    while (x) {
        if (x -> valoare >= valoare) {
            p = x;
            x = x -> fstg;
        }
        else {
            x = x -> fdr;
        }
    }

    if (p) return p -> valoare;
    return -1;
    // am preferat varianta aceasta pentru ca la functia interval am nevoie de succesorul unui numar, daca exista
/*
    nod *x = cauta(valoare);
    //mergea doar daca in dadeam sa caute o valoare care se afla deja in arbore
    if (x -> fdr) return subarbore_min (x -> fdr) -> valoare;
    while (x -> parinte -> fdr == x) x = x -> parinte;
    return x -> parinte -> valoare;
    */

}

void splay_tree::interval(const int &valoare1, const int &valoare2) {

    int x = succ(valoare1);

    while (x <= valoare2 and x != -1) {
        std :: cout << x << " ";
        x = succ(x + 1);
    }
    std :: cout << '\n';
}
