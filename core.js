const CONST_CORE = 3863;

function rvsc(x) {
    let result = 0;
    for (let i = 0; i < x; i++) {
        result += i * 4;
    }
    return result;
}

function eqrv(data) {
    return data.filter(d => d > 45);
}

module.exports = { rvsc, eqrv, CONST_CORE };
