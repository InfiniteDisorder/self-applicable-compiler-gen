def E(node):
    if len(node.children) == 3:
        fst_arg = node.children[0]
        op = node.children[1]
        scd_arg = node.children[2]

        if fst_arg.marker == 'E' and scd_arg.marker == 'T':
            if op.marker.domain == 'plus':
                return E(fst_arg) + T(scd_arg)

            if op.marker.domain == 'minus':
                return E(fst_arg) - T(scd_arg)

    if len(node.children) == 1 and node.children[0].marker == 'T':
        return T(node.children[0])


def T(node):
    if len(node.children) == 3:
        fst_arg = node.children[0]
        op = node.children[1]
        scd_arg = node.children[2]

        if fst_arg.marker == 'T' and scd_arg.marker == 'F':
            if op.marker.domain == 'mul':
                return T(fst_arg) * F(scd_arg)

            if op.marker.domain == 'div':
                return T(fst_arg) / F(scd_arg)

    if len(node.children) == 1 and node.children[0].marker == 'F':
        return F(node.children[0])


def F(node):
    if len(node.children) == 1 and node.children[0].marker.domain == 'n':
        return int(node.children[0].marker.image)

    if len(node.children) == 3:
        fst_arg = node.children[0]
        scd_arg = node.children[1]
        thd_arg = node.children[2]

        if fst_arg.marker.domain == 'lparen' and \
           scd_arg.marker == 'E' and \
           thd_arg.marker.domain == 'rparen':
            return E(scd_arg)


def traverse(tree):
    return E(tree)
