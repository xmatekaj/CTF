const cipher_str = "264,889,119,374,559,357,870,453,4ce,264,77,a5d,87a,170,77,87a,b5a,a5d,119,87a,87a,b5a,2b2,170,96c,70a,77,7aa,870,b5a,6ed,170,5ec";
const values = cipher_str.split(',');

// Convert all hex to decimal
const ciphertext = values.map(x => parseInt(x, 16));
console.log("Ciphertext values (all treated as hex):", ciphertext);

// Calculate private key
const p = 61;
const q = 53;
const n = p * q;
const totient = (p-1) * (q-1);
const e = 17;

function modInverse(e, phi) {
    let [old_r, r] = [e, phi];
    let [old_s, s] = [1, 0];
    let [old_t, t] = [0, 1];

    while (r !== 0) {
        const quotient = Math.floor(old_r / r);
        [old_r, r] = [r, old_r - quotient * r];
        [old_s, s] = [s, old_s - quotient * s];
        [old_t, t] = [t, old_t - quotient * t];
    }

    return old_s < 0 ? old_s + phi : old_s;
}

const d = modInverse(e, totient);
console.log("Private exponent d:", d);

// Decrypt function
function modPow(base, exponent, modulus) {
    if (modulus === 1) return 0;
    let result = 1n;
    base = BigInt(base);
    exponent = BigInt(exponent);
    modulus = BigInt(modulus);
    
    while (exponent > 0n) {
        if (exponent % 2n === 1n) {
            result = (result * base) % modulus;
        }
        base = (base * base) % modulus;
        exponent = exponent / 2n;
    }
    return Number(result);
}

// Decrypt each value
const decrypted = ciphertext.map(c => modPow(c, d, n));
console.log("Decrypted values:", decrypted);

// Convert to ASCII
const message = String.fromCharCode(...decrypted);
console.log("Decrypted message:", message);