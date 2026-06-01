def calfp(frates, fac_rate):
    # Tablice pomocnicze (w Pythonie listy), odpowiadające tym z C++
    fun_units = [
        "External Inputs",
        "External Outputs",
        "External Inquiries",
        "Internal Logical Files",
        "External Interface Files"
    ]
    
    wt_rates = ["Low", "Average", "High"]
    
    # Wagi czynników (Weight Factors)
    wt_factors = [
        [3, 4, 6],
        [4, 5, 7],
        [3, 4, 6],
        [7, 10, 15],
        [5, 7, 10]
    ]
    
    ufp = 0
    
    # Obliczanie UFP (Unadjusted Function Point)
    for i in range(5):
        for j in range(3):
            freq = frates[i][j]
            ufp += freq * wt_factors[i][j]
            
    # 14 czynników ogólnych (w Pythonie zachowane dla kompletności struktury kodu)
    aspects = [
        "reliable backup and recovery required ?",
        "data communication required ?",
        "are there distributed processing functions ?",
        "is performance critical ?",
        "will the system run in an existing heavily utilized operational environment ?",
        "on line data entry required ?",
        "does the on line data entry require the input transaction to be built over multiple screens or operations ?",
        "are the master files updated on line ?",
        "is the inputs, outputs, files or inquiries complex ?",
        "is the internal processing complex ?",
        "is the code designed to be reusable ?",
        "are the conversion and installation included in the design ?",
        "is the system designed for multiple installations in different organizations ?",
        "is the application designed to facilitate change and ease of use by the user ?"
    ]
    
    # Obliczanie sumy ocen czynników (sumF)
    sum_f = 0
    for i in range(14):
        rate = fac_rate
        sum_f += rate
        
    # Obliczanie CAF (Complexity Adjustment Factor)
    caf = 0.65 + 0.01 * sum_f
    
    # Obliczanie ostatecznych Punktów Funkcyjnych (FP)
    fp = ufp * caf
    
    # Wyświetlanie wyników (zaokrąglone dla estetyki do 2 miejsc po przecinku)
    print("Function Point Analysis :-")
    print(f"Unadjusted Function Points (UFP) : {ufp}")
    print(f"Complexity Adjustment Factor (CAF) : {caf:.2f}")
    print(f"Function Points (FP) : {fp:.2f}")

# Główna funkcja sterująca (odpowiednik int main())
if __name__ == "__main__":
    frates = [
        [1, 4, 6],
        [0, 0, 6],
        [3, 1, 0],
        [4, 2, 2],
        [1, 0, 0]
    ]
    
    fac_rate = 2
    
    calfp(frates, fac_rate)
