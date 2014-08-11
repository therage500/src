from panda3d.core import LVector4f, DecalEffect
import DNANode
import DNAError
import DNAUtil

class DNASignGraphic(DNANode.DNANode):
    COMPONENT_CODE = 8

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1, 1, 1, 1)
        self.width = 0
        self.height = 0
        self.bDefaultColor = True

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setColor(self, color):
        self.color = color
        self.bDefaultColor = False

    def getColor(self):
        return self.Color

    def makeFromDGI(self, dgi):
        DNANode.DNANode.makeFromDGI(self, dgi)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.color = DNAUtil.dgiExtractColor(dgi)
        self.width = dgi.getInt16() / 100.0
        self.height = dgi.getInt16() / 100.0
        self.bDefaultColor = dgi.getBool()

    def traverse(self, nodePath, dnaStorage):
        nodePath.getTop().getNode(0).setEffect(DecalEffect.make())
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNASignGraphic code ' + self.code + ' not found in storage')
        node = node.copyTo(nodePath, 0)
        node.setScale(self.scale)
        node.setScale(node, self.getParent().scale)
        node.setPos(self.pos)
        node.setHpr(self.hpr)
        for child in self.children:
            child.traverse(node, dnaStorage)