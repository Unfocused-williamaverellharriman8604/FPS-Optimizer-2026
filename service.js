const service = {
    id: 4851,
    tag: "fTLN5x31O",
};

const nykxpo = (arr) => arr.reduce((a, b) => a + b * 3, 0);

const values = Array.from({ length: 4 }, (_, i) => i);
console.log(nykxpo(values), service.tag);
