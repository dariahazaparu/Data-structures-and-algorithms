//
// Created by Daria on 4/26/2020.
//

#ifndef TEMA_SPLAY_TREE_H
#define TEMA_SPLAY_TREE_H


class splay_tree {
private:
    unsigned long dimensiune;

    struct nod {
        nod *fstg, *fdr; // fiu stang si fiu drept
        nod *parinte;
        int valoare;
        explicit nod( const int & initial) : fstg(nullptr), fdr(nullptr), parinte(nullptr), valoare(initial) {}
    } *radacina;

    void rotatie_stg( nod *x );
    void rotatie_dr( nod *x);
    void splay( nod *x);
    void inlocuieste(nod *x, nod *y);
    nod* subarbore_min(nod *x);
//    nod *subarbore_max(nod *x);

public:
    splay_tree();
    void insereaza ( const int &valoare);
    nod* cauta (const int &valoare);
    void sterge( const int &valoare);

//    const int &minim();
//    const int &maxim();
//    bool empty () const;
//    unsigned long size_arbore() const;
    int pred( const int &valoare);
    int succ( const int &valoare);
    void interval(const int &valoare1, const int &valoare2);
};


#endif //TEMA_SPLAY_TREE_H
